import { Component, OnInit } from '@angular/core';
import { AlertController, ModalController } from '@ionic/angular';
import { RestaurantAppService } from 'src/app/services/restaurant-app.service';

@Component({
  selector: 'app-ip-global',
  templateUrl: './ip-global.component.html',
  styleUrls: ['./ip-global.component.scss'],
})
export class IpGlobalComponent implements OnInit {
  
  ipApi = "";
  constructor(private modalcrontroller: ModalController,private servicioRestaurant: RestaurantAppService,public alertController: AlertController) { }
  ngOnInit() {}

  dismissModal() {
    this.modalcrontroller.dismiss({
      'dismissed': true
    });
  }

  asignarIpApi(){
    if (!(this.ipApi == "")) {
      this.servicioRestaurant.PonerIPServicio(this.ipApi);
      this.dismissModal()
      this.presentAlert("Exito", "Ip Ingresada Correctamente");
    }else{
      this.presentAlert("Error", "Ingrese Datos");
    }
  }

  async presentAlert(header, message) {
    const alert = await this.alertController.create({
      cssClass: 'my-custom-class',
      header: header,
      message: message,
      buttons: ['OK']
    });

    await alert.present();

    const { role } = await alert.onDidDismiss();
  }

}
