namespace JanusFrontend
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            sidePanel = new PictureBox();
            btnCreateNewDataset = new PictureBox();
            btnOpenExistingSet = new PictureBox();
            btnPopplerDownloads = new PictureBox();
            prgDownloading = new ProgressBar();
            btnViewConsole = new PictureBox();
            lblProgress = new Label();
            ((System.ComponentModel.ISupportInitialize)sidePanel).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnCreateNewDataset).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnOpenExistingSet).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnPopplerDownloads).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnViewConsole).BeginInit();
            SuspendLayout();
            // 
            // sidePanel
            // 
            sidePanel.BackgroundImage = Properties.Resources.HomeDownloading;
            sidePanel.BackgroundImageLayout = ImageLayout.Zoom;
            sidePanel.Location = new Point(0, 0);
            sidePanel.Name = "sidePanel";
            sidePanel.Size = new Size(255, 700);
            sidePanel.TabIndex = 0;
            sidePanel.TabStop = false;
            // 
            // btnCreateNewDataset
            // 
            btnCreateNewDataset.BackColor = Color.White;
            btnCreateNewDataset.BackgroundImageLayout = ImageLayout.None;
            btnCreateNewDataset.Image = (Image)resources.GetObject("btnCreateNewDataset.Image");
            btnCreateNewDataset.Location = new Point(8, 170);
            btnCreateNewDataset.Name = "btnCreateNewDataset";
            btnCreateNewDataset.Size = new Size(165, 31);
            btnCreateNewDataset.SizeMode = PictureBoxSizeMode.StretchImage;
            btnCreateNewDataset.TabIndex = 1;
            btnCreateNewDataset.TabStop = false;
            btnCreateNewDataset.Click += btnCreateNewDataset_Click;
            // 
            // btnOpenExistingSet
            // 
            btnOpenExistingSet.BackColor = Color.White;
            btnOpenExistingSet.BackgroundImageLayout = ImageLayout.None;
            btnOpenExistingSet.Image = (Image)resources.GetObject("btnOpenExistingSet.Image");
            btnOpenExistingSet.Location = new Point(8, 205);
            btnOpenExistingSet.Name = "btnOpenExistingSet";
            btnOpenExistingSet.Size = new Size(145, 31);
            btnOpenExistingSet.SizeMode = PictureBoxSizeMode.StretchImage;
            btnOpenExistingSet.TabIndex = 2;
            btnOpenExistingSet.TabStop = false;
            btnOpenExistingSet.Click += btnOpenExistingSet_Click;
            // 
            // btnPopplerDownloads
            // 
            btnPopplerDownloads.BackColor = Color.White;
            btnPopplerDownloads.BackgroundImageLayout = ImageLayout.None;
            btnPopplerDownloads.Image = (Image)resources.GetObject("btnPopplerDownloads.Image");
            btnPopplerDownloads.Location = new Point(8, 170);
            btnPopplerDownloads.Name = "btnPopplerDownloads";
            btnPopplerDownloads.Size = new Size(202, 31);
            btnPopplerDownloads.SizeMode = PictureBoxSizeMode.StretchImage;
            btnPopplerDownloads.TabIndex = 3;
            btnPopplerDownloads.TabStop = false;
            btnPopplerDownloads.Visible = false;
            // 
            // prgDownloading
            // 
            prgDownloading.ForeColor = Color.FromArgb(193, 99, 202);
            prgDownloading.Location = new Point(8, 170);
            prgDownloading.MarqueeAnimationSpeed = 33;
            prgDownloading.Name = "prgDownloading";
            prgDownloading.Size = new Size(236, 20);
            prgDownloading.Style = ProgressBarStyle.Marquee;
            prgDownloading.TabIndex = 4;
            prgDownloading.Visible = false;
            // 
            // btnViewConsole
            // 
            btnViewConsole.BackColor = Color.White;
            btnViewConsole.BackgroundImageLayout = ImageLayout.None;
            btnViewConsole.Image = (Image)resources.GetObject("btnViewConsole.Image");
            btnViewConsole.Location = new Point(8, 569);
            btnViewConsole.Name = "btnViewConsole";
            btnViewConsole.Size = new Size(114, 31);
            btnViewConsole.SizeMode = PictureBoxSizeMode.StretchImage;
            btnViewConsole.TabIndex = 5;
            btnViewConsole.TabStop = false;
            btnViewConsole.Visible = false;
            btnViewConsole.Click += btnViewConsole_Click;
            // 
            // lblProgress
            // 
            lblProgress.AutoSize = true;
            lblProgress.BackColor = Color.White;
            lblProgress.Font = new Font("Segoe UI", 10.5F, FontStyle.Bold);
            lblProgress.Location = new Point(7, 167);
            lblProgress.Name = "lblProgress";
            lblProgress.Size = new Size(159, 19);
            lblProgress.TabIndex = 6;
            lblProgress.Text = "0/0 images processed.";
            lblProgress.Visible = false;
            lblProgress.Click += label1_Click;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(970, 612);
            Controls.Add(lblProgress);
            Controls.Add(btnViewConsole);
            Controls.Add(prgDownloading);
            Controls.Add(btnPopplerDownloads);
            Controls.Add(btnOpenExistingSet);
            Controls.Add(btnCreateNewDataset);
            Controls.Add(sidePanel);
            Icon = (Icon)resources.GetObject("$this.Icon");
            MaximumSize = new Size(986, 651);
            Name = "MainForm";
            Text = "transitIOM Janus";
            ((System.ComponentModel.ISupportInitialize)sidePanel).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnCreateNewDataset).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnOpenExistingSet).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnPopplerDownloads).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnViewConsole).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox sidePanel;
        private PictureBox btnCreateNewDataset;
        private PictureBox btnOpenExistingSet;
        private PictureBox btnPopplerDownloads;
        private ProgressBar prgDownloading;
        private PictureBox btnViewConsole;
        private Label lblProgress;
    }
}