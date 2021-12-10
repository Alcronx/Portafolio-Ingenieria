import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { AlertController, ModalController } from '@ionic/angular';
import { RestaurantAppService } from 'src/app/services/restaurant-app.service';
import { DatosMesero,DatosOrdenCliente } from '../../interfaces/interfaces';

@Component({
  selector: 'app-modal-mesas',
  templateUrl: './modal-mesas.component.html',
  styleUrls: ['./modal-mesas.component.scss'],
})
export class ModalMesasComponent implements OnInit {

  constructor(private modalcrontroller: ModalController,private servicioRestaurant: RestaurantAppService,public alertController: AlertController,private router: Router) { }
  @Input() meseros: DatosMesero[] = [];
  @Input() ordenesCliente: DatosOrdenCliente[] = [];
  @Input() idClienteMesa = "";
  @Input() idMesa = "";
  ngOnInit() { 
    this.totalBoleta();
  }

  dismissModal() {
    this.modalcrontroller.dismiss({
      'dismissed': true
    });
  }

  totalBoleta() : number{
    let total = 0;
    for (let i of this.ordenesCliente) {
      total += i.TOTAL
    }
    return total
  }

  pagarOrden(idCliente,idmesa){
    this.servicioRestaurant.pagarOrdenCliente({ 'idMesa': idmesa, 'idCliente': idCliente }).subscribe(resp => {
      if (resp == 1) {
        this.presentAlert("Exito", "Orden Pagada Correctamente");
      }
      if (resp == -1) {
        this.presentAlert("Error", "Error en la base de datos");
      }
      if (resp == 0) {
        this.presentAlert("Error", "Error al enviar datos a la api");
      }
    })
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

  async presentAlertConfirm(idClienteMesa,idMesa) {
    const alert = await this.alertController.create({
      cssClass: 'my-custom-class',
      header: 'Pago',
      message: 'Confirmar Pago De Orden',
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          cssClass: 'secondary',
          handler: (blah) => {
          }
        }, {
          text: 'Confirmar',
          handler: () => {
            this.pagarOrden(idClienteMesa,idMesa)
            this.router.navigateByUrl("/mesero")
            this.dismissModal()
          }
        }
      ]
    });

    await alert.present();
  }

}




