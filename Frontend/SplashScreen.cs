using System.Threading.Tasks;

namespace JanusFrontend
{
    public partial class SplashScreen : Form
    {
        public SplashScreen()
        {
            InitializeComponent();
        }

        private async void SplashScreen_Load(object sender, EventArgs e)
        {
            // look for user data file

            await Task.Delay(1500); // simulate loading
            Program.SwitchMain(new MainForm());
        }
    }
}
