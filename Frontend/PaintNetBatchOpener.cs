using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace JanusFrontend
{
    public sealed class PaintNetBatchOpener
    {
        private const string PaintProcessName = "PaintDotNet";
        private const int DelayMs = 1500; // fixed 1.5s
        private readonly string _rootFolder;

        public PaintNetBatchOpener(string rootFolder)
        {
            _rootFolder = Path.GetFullPath(rootFolder);
        }

        public sealed class ItemCompletedEventArgs : EventArgs
        {
            public int Index { get; }
            public int Total { get; }
            public string FilePath { get; }
            public ItemCompletedEventArgs(int index, int total, string filePath)
            {
                Index = index; Total = total; FilePath = filePath;
            }
        }

        public sealed class BatchCompletedEventArgs : EventArgs
        {
            public int Total { get; }
            public BatchCompletedEventArgs(int total) { Total = total; }
        }

        public event EventHandler<ItemCompletedEventArgs>? ItemCompleted;
        public event EventHandler<BatchCompletedEventArgs>? BatchCompleted;

        public async Task OpenAllAsync(CancellationToken ct = default)
        {
            var files = EnumeratePngs(_rootFolder);
            int total = files.Count;

            for (int i = 0; i < total; i++)
            {
                ct.ThrowIfCancellationRequested();
                string file = files[i];

                // Ensure no existing Paint.NET instance so wait logic is deterministic
                await WaitForPaintNetToExitAsync(ct);

                // Open PNG
                OpenInPaintDotNetViaProtocol(file);

                // Wait until user closes Paint.NET
                await WaitForPaintNetToExitAsync(ct);

                // Notify UI: one file completed (index is 1-based)
                ItemCompleted?.Invoke(this, new ItemCompletedEventArgs(i + 1, total, file));

                // Fixed delay
                await Task.Delay(DelayMs, ct);
            }

            // Notify UI: batch done
            BatchCompleted?.Invoke(this, new BatchCompletedEventArgs(total));
        }

        private List<string> EnumeratePngs(string folder)
        {
            var list = new List<string>();
            if (!Directory.Exists(folder)) return list;
            foreach (var path in Directory.EnumerateFiles(folder, "*.png", SearchOption.AllDirectories))
                list.Add(path);
            return list;
        }

        private static void OpenInPaintDotNetViaProtocol(string filePath)
        {
            string full = Path.GetFullPath(filePath);
            string args = $"/c start \"\" \"paintdotnet:{full}\"";
            var psi = new ProcessStartInfo
            {
                FileName = "cmd.exe",
                Arguments = args,
                UseShellExecute = false,
                CreateNoWindow = true,
                WindowStyle = ProcessWindowStyle.Hidden
            };
            Process.Start(psi);
        }

        private static async Task WaitForPaintNetToExitAsync(CancellationToken ct)
        {
            while (IsPaintNetRunning())
            {
                ct.ThrowIfCancellationRequested();
                await Task.Delay(200, ct);
            }
        }

        private static bool IsPaintNetRunning()
        {
            try { return Process.GetProcessesByName(PaintProcessName).Length > 0; }
            catch { return true; }
        }
    }
}
