using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace JanusFrontend
{
    internal static class BackendHandler
    {
        public static bool StdoutPopplerErrorRegex()
        {
            Regex rx = new(
                @"^\[\d+/\d+\]\s+error converting .*\.pdf:\s+Unable to get page count\. Is poppler installed and in PATH\?$",
                RegexOptions.IgnoreCase | RegexOptions.CultureInvariant);

            while (true)
            {
                var buf = Program.backend.GetFullOutput();
                if (!string.IsNullOrEmpty(buf))
                {
                    int nl = buf.IndexOf('\n');
                    string line = nl >= 0 ? buf.Substring(0, nl) : buf;
                    line = line.TrimEnd('\r');

                    if (line.Length > 0)
                        return rx.IsMatch(line);
                }
                Thread.Sleep(25); // light poll; run off-UI thread
            }
        }
    }
}

