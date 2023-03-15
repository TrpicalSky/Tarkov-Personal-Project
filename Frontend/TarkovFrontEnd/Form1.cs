using System.Diagnostics;
using System.Net.Http.Json;
using System.Net;
using static System.Net.WebRequestMethods;
using System.Text.Json;
using Newtonsoft.Json.Linq;

namespace TarkovFrontEnd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        async private void button1_Click(object sender, EventArgs e)
        {
            string iconLink;
            string item = "M.U.L.E";
            string url = "http://127.0.0.1:5000/?item=" + item;

            using var client = new HttpClient();
            var content = await client.GetAsync(url);
            content.EnsureSuccessStatusCode();
            var responseBody = await content.Content.ReadAsStringAsync();
            var myJObject = JObject.Parse(responseBody);
            try
            {
                iconLink = myJObject.SelectToken("data").SelectToken("items").SelectToken("iconLink").ToString();
                var icon = new Bitmap(iconLink);
                pictureBox1.Image = icon;
            } catch (Exception ex)
            {
                iconLink = "";
                Debug.WriteLine(ex.Message);
            }
            
            

            Debug.WriteLine(myJObject.SelectToken("data").SelectToken("items"));

        }
    }
}