using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Net.Sockets; //Para enviar datos.
using System.Net;
using Tobii.Interaction.Wpf;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Dynamic;

namespace TobiiWPF
{
    public partial class MainWindow : Window
    {
        public Boolean conductorPendiente = false;
        private Socket servidor;
        private String ip;
        private int puerto;
        
        public MainWindow()
        {
            InitializeComponent();


            //Inicializacion del servidor
            this.servidor = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);



            
        }

        public void enviaEstadoConductor()
        {
            try
            {
                IPAddress serverAddr = IPAddress.Parse(this.ip);
                IPEndPoint endPoint = new IPEndPoint(serverAddr, this.puerto);

                string estadoConductor = this.conductorPendiente.ToString();

                byte[] buffer = Encoding.ASCII.GetBytes(estadoConductor);
                this.servidor.SendTo(buffer, endPoint);
                Console.WriteLine("Se ha enviado un paquete UDP: " + estadoConductor);
            }
            catch
            {
                IPAddress serverAddr = IPAddress.Parse("127.0.0.1");
                IPEndPoint endPoint = new IPEndPoint(serverAddr, 1234);

                string estadoConductor = this.conductorPendiente.ToString();

                byte[] buffer = Encoding.ASCII.GetBytes(estadoConductor);
                this.servidor.SendTo(buffer, endPoint);
                Console.WriteLine("Se ha enviado un paquete UDP: " + estadoConductor);
            }
        }

        private void LayoutRoot_funciontobii(object sender, HasGazeChangedRoutedEventArgs e)
        {
            if (e.HasGaze)
            {
                this.conductorPendiente = true;
            }
            else
            {
                this.conductorPendiente = false;
            }
            enviaEstadoConductor();



        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            TextBox tb = sender as TextBox;
            Console.WriteLine("Se ha cambiado la ip: "+tb.Text);
            this.ip = tb.Text;
        }

        private void TextBox_TextChanged_1(object sender, TextChangedEventArgs e)
        {
            TextBox tb = sender as TextBox;
            Console.WriteLine("Se ha cambiado el puerto: " + tb.Text);
            this.puerto = Int32.Parse(tb.Text);
        }



    }

}
