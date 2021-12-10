import { Component, OnInit } from '@angular/core';
import { AlertController } from '@ionic/angular';
import { Mesa, Mesero, MenuRestaurant, MenuRestaurantCarrito, OrderClient } from 'src/app/interfaces/interfaces';
import { RestaurantAppService } from 'src/app/services/restaurant-app.service';

@Component({
  selector: 'app-orden',
  templateUrl: './orden.page.html',
  styleUrls: ['./orden.page.scss'],
})
export class OrdenPage implements OnInit {
  menus: MenuRestaurant[] = [];
  mesero: Mesero[] = [];
  mesa: Mesa[] = [];
  menuCarrito: MenuRestaurantCarrito;
  DatosSelectCarrito = []
  carritoOrden = [];
  idMesero = "";
  idCliente = "";
  totalCarrito = 0;
  constructor(private servicioRestaurant: RestaurantAppService, public alertController: AlertController) { }

  ngOnInit() {
    this.servicioRestaurant.obtenerMenuProducto().subscribe(resp => {
      this.menus.push(...Object.values(resp))
      let m = Object.values(resp)[0];
    })
    this.servicioRestaurant.obtenerMesa().subscribe(resp => {
      this.mesa.push(...Object.values(resp))
    })
    this.servicioRestaurant.obtenerMeseros().subscribe(resp => {
      this.mesero.push(...Object.values(resp))
    })
    this.carritoOrden = this.servicioRestaurant.obtenerCarrito();
  }

  agregarAlCarro() {
    this.menuCarrito = new MenuRestaurantCarrito();
    var objetoCarrito = Object.values(this.DatosSelectCarrito)
    if (objetoCarrito.length != 0) {
      this.menuCarrito.menuid = objetoCarrito[0];
      this.menuCarrito.name = objetoCarrito[1];
      this.menuCarrito.menuPrice = objetoCarrito[2];
      this.menuCarrito.quantity = 1;
      this.menuCarrito.total = objetoCarrito[2] * 1;
      this.servicioRestaurant.agregarProducto(this.menuCarrito);
      this.retornarTotalCarrito()
    } else {
      this.presentAlert("Error", "Agregue un producto");
    }
  }

  bajarCantidad(producto) {
    this.servicioRestaurant.bajarCantidadProducto(producto);
    this.retornarTotalCarrito()
  }

  subirCantidad(producto) {
    this.servicioRestaurant.agregarProducto(producto);
    this.retornarTotalCarrito()
  }

  retornarTotalCarrito() {
    let total = 0;
    for (let [index, p] of this.carritoOrden.entries()) {
      total = total + p.total
    }
    this.totalCarrito = total
  }

  cancelarOrden() {
    this.servicioRestaurant.eliminarCarrito();
    this.carritoOrden = this.servicioRestaurant.obtenerCarrito();
    this.totalCarrito = 0;
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

  guardarOrdenCliente() {
    let oc = new OrderClient();
    let ocd = this.carritoOrden;
    oc.idMesero = parseInt(this.idMesero);
    oc.idCliente = parseInt(this.idCliente);
    oc.totalCarrito = this.totalCarrito;
    oc.OrderClientDetails = ocd;
    if (!(this.carritoOrden.length == 0, this.idMesero == "", this.idCliente == "", this.totalCarrito == 0)) {
      this.servicioRestaurant.agregarOrdenCliente(oc).subscribe(resp => {
        if (resp == 1) {
          this.presentAlert("Exito", "Orden Agregada Correctamente");
        }
        if (resp == -1) {
          this.presentAlert("Error", "Error en la base de datos");
        }
        if (resp == 0) {
          this.presentAlert("Error", "Error al enviar datos a la api");
        }
        this.cancelarOrden();
      })
    } else {
      this.presentAlert("Error", "Agregue un producto");
    }


  }




}
