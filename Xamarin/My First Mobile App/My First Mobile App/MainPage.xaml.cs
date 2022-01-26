using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace My_First_Mobile_App
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        public void CalculatorButton(object sender, EventArgs e)
        {
            DisplayAlert("Calculator", "Under Maintenance", "OK");
        }
    }
}
