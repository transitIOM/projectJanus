using System;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Threading.Tasks;

namespace JanusFrontend
{
    internal class Backend : IDisposable
    {
        private readonly static string _scriptPath = @"C:\Coding\janus\projectJanus\src\main.py";
        private readonly string _venvPath;
        private readonly ProcessStartInfo _psi;

        private Process? _proc;
        private string? _lastOutputLine;

        private readonly StringBuilder _stdoutBuffer = new();
        private readonly StringBuilder _stderrBuffer = new();
        private readonly object _sync = new();

        public event EventHandler<string>? OutputLineReceived;
        public event EventHandler<string>? ErrorLineReceived;

        public bool IsRunning => _proc is { HasExited: false };

        public Backend()
        {
            _venvPath = Path.Combine(Path.GetDirectoryName(_scriptPath)!, ".venv");

            _psi = new ProcessStartInfo
            {
                Arguments = "",                 // filled in Start by method caller
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                RedirectStandardInput = true,
                CreateNoWindow = true,
                StandardOutputEncoding = Encoding.UTF8,
                StandardErrorEncoding = Encoding.UTF8,
                WorkingDirectory = Path.GetDirectoryName(_scriptPath)!
            };
        }

        public async Task StartAsync(string? arguments = null)
        {
            if (IsRunning) return;

            if (!Directory.Exists(_venvPath))
            {
                await CreateVenvAsync(_venvPath);
            }

            var pythonExe = Path.Combine(_venvPath, "Scripts", "python");
            if (!File.Exists(pythonExe))
            {
                pythonExe = "py"; //fallback hail mary
            }

            _psi.FileName = pythonExe;
            var userArgs = string.IsNullOrWhiteSpace(arguments) ? "" : " " + arguments;
            _psi.Arguments = $"\"{_scriptPath}\"{userArgs}";

            _proc = new Process { StartInfo = _psi, EnableRaisingEvents = true };

            _proc.OutputDataReceived += (s, e) =>
            {
                if (e.Data is null) return;
                lock (_sync)
                {
                    _stdoutBuffer.AppendLine(e.Data);
                    _lastOutputLine = e.Data;
                }
                OutputLineReceived?.Invoke(this, e.Data);
            };

            _proc.ErrorDataReceived += (s, e) =>
            {
                if (e.Data is null) return;
                lock (_sync)
                {
                    _stderrBuffer.AppendLine(e.Data);
                }
                ErrorLineReceived?.Invoke(this, e.Data);
            };

            _proc.Start();
            _proc.BeginOutputReadLine(); 
            _proc.BeginErrorReadLine();  
        }

        private async Task CreateVenvAsync(string venvPath)
        {
            Directory.CreateDirectory(Path.GetDirectoryName(venvPath)!);
            var psi = new ProcessStartInfo
            {
                FileName = "py",
                Arguments = $"-m venv \"{venvPath}\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };

            using var p = new Process { StartInfo = psi };
            p.Start();
            await p.WaitForExitAsync().ConfigureAwait(false);
        }

        public async Task WriteLineAsync(string line)
        {
            if (_proc is null || _proc.HasExited)
                throw new InvalidOperationException("Process is not running.");

            await _proc.StandardInput.WriteLineAsync(line).ConfigureAwait(false);
            await _proc.StandardInput.FlushAsync().ConfigureAwait(false);
        }

        public void CloseInput() => _proc?.StandardInput.Close();

        public string? ReadLastLine()
        {
            lock (_sync) return _lastOutputLine;
        }

        public string GetFullOutput()
        {
            lock (_sync) return _stdoutBuffer.ToString();
        }

        public string GetFullError()
        {
            lock (_sync) return _stderrBuffer.ToString();
        }

        public void ClearBuffers()
        {
            lock (_sync)
            {
                _stdoutBuffer.Clear();
                _stderrBuffer.Clear();
                _lastOutputLine = null;
            }
        }

        public Task WaitForExitAsync() =>
            _proc is null ? Task.CompletedTask : _proc.WaitForExitAsync();

        public void Dispose()
        {
            if (_proc is null) return;
            try
            {
                if (!_proc.HasExited) _proc.Kill(true);
            }
            catch { Debug.WriteLine("Error: Failed to kill backend process."); }
            finally
            {
                _proc.Dispose();
                _proc = null;
            }
        }
    }
}
