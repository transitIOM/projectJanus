using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace JanusFrontend
{
    public partial class MainForm : Form
    {
        private string datasetFolder;
        private PaintNetBatchOpener? _opener;
        public MainForm()
        {
            InitializeComponent();
            datasetFolder = "";

            sidePanel.BackgroundImage = Properties.Resources.HomeProjPick;
            btnCreateNewDataset.Visible = true;
            btnOpenExistingSet.Visible = true;
        }

        private string DatasetPicker(string message)
        {
            string projectDirectory = Path.Combine(Program.rootJanusPath, "datasets");
            Directory.CreateDirectory(projectDirectory);

            string chosenFolder = "";
            using (FolderBrowserDialog dlg = new())
            {
                dlg.Description = message;
                dlg.UseDescriptionForTitle = true;
                dlg.SelectedPath = projectDirectory;
                dlg.ShowNewFolderButton = true;

                if (dlg.ShowDialog(this) == DialogResult.OK)
                {
                    chosenFolder = dlg.SelectedPath;
                }
            }
            return chosenFolder;
        }

        private async void btnCreateNewDataset_Click(object sender, EventArgs e)
        {
            datasetFolder = DatasetPicker("Create dataset folder");
            MessageBox.Show("Running the python process doesnt work yet so just go run it yourself so it downloads the files and click view console to simulate it finishing. Janky I know.");
            //await Program.backend.StartAsync(/* args for folder choice will go here ig once backend supports */);
            btnCreateNewDataset.Visible = false;
            btnOpenExistingSet.Visible = false;
            sidePanel.BackgroundImage = Properties.Resources.HomeDownloading;
            prgDownloading.Visible = true;
            btnViewConsole.Visible = true;


            //bool isPopplerNotInstalled = await Task.Run(() => BackendHandler.StdoutPopplerErrorRegex());

            //if (isPopplerNotInstalled)
            //{
            //    Program.backend.Dispose();

            //    btnViewConsole.Visible = false;
            //    btnPopplerDownloads.Visible = true;
            //    sidePanel.BackgroundImage = Properties.Resources.HomePopplerErr;
            //}
        }

        private void btnOpenExistingSet_Click(object sender, EventArgs e)
        {
            datasetFolder = DatasetPicker("Open dataset folder");

            // from here we will rely on log files to see where in the process the dataset is up to

            throw new NotImplementedException(message: "No current way to open existing datasets and modify/resume");
        }

        private async void btnViewConsole_Click(object sender, EventArgs e)
        {
            sidePanel.BackgroundImage = Properties.Resources.HomePaintNET;
            prgDownloading.Visible = false;
            btnViewConsole.Visible = false;
            lblProgress.Visible = true;

            _opener = new PaintNetBatchOpener(@"C:\Coding\janus\projectJanus\tempdata\images");

            _opener.ItemCompleted += (s, a) =>
                BeginInvoke(new Action(() =>
                    lblProgress.Text = $"{a.Index}/{a.Total} images processed."));

            _opener.BatchCompleted += (s, a) =>
                BeginInvoke(new Action(() =>
                {
                    lblProgress.Text = $"{a.Total}/{a.Total} done";
                    MessageBox.Show(this, "All images processed.", "Done");
                }));

            await _opener.OpenAllAsync();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
