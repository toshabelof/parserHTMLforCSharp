using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AngleSharp.Parser.Html;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var parser = new HtmlParser();
            string pSite = tBoxSite.Text;
            var doc = parser.Parse(pSite);


            dataGridView1.Rows.Add();
            dataGridView1.Rows[0].Cells[0].Value = pSite;
        }
    }
}
