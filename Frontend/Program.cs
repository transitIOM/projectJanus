namespace JanusFrontend
{


    internal static class Program
    {
        public static Backend backend = new();
        public static ApplicationContext appCtx;
        public static string rootJanusPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "transitIOM Janus");
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            appCtx = new ApplicationContext(new SplashScreen());
            Application.Run(appCtx);
        }
        public static void SwitchMain(Form newForm)
        {
            var old = appCtx.MainForm;
            appCtx.MainForm = newForm; 
            newForm.Show();
            old?.Close();
        }
    }
}