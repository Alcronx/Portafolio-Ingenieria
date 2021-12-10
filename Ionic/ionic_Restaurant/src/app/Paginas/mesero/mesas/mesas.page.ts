import { Component, OnInit } from '@angular/core';
import { async, waitForAsync } from '@angular/core/testing';
import { ModalController } from '@ionic/angular';
import { ModalMesasComponent } from 'src/app/componentes/modal-mesas/modal-mesas.component';
import { Mesa, DatosMesero, DatosOrdenCliente } from 'src/app/interfaces/interfaces';
import { RestaurantAppService } from 'src/app/services/restaurant-app.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-mesas',
  templateUrl: './mesas.page.html',
  styleUrls: ['./mesas.page.scss'],
})
export class MesasPage implements OnInit {

  constructor(public modalController: ModalController, private servicioRestaurant: RestaurantAppService) { }
  mesa: Mesa[] = [];


  ngOnInit() {
    this.servicioRestaurant.obtenerMesa().subscribe(resp => {
      this.mesa.push(...Object.values(resp))
    })
    console.log("wena")
  }

  async mostrarModalMesas(idCliente, idMesa) {
    let datosMeseros = await this.obtenerDatosmesero(idCliente);
    let ordenesCliente = await this.obtenerOrdenesCliente(idCliente);  
    const modal = await this.modalController.create({
      component: ModalMesasComponent,
      cssClass: 'my-custom-class',
      componentProps: {
        //ObtendraDatosMesero
        'meseros': datosMeseros,
        //ObtendraDatosOrdenCliente
        'ordenesCliente': ordenesCliente,
        //ObtendraDatosOrdenCliente
        'idClienteMesa' : idCliente,
        //ObtendraDatosOrdenCliente
        'idMesa' : idMesa
      }
    });
    return await modal.present();
  }

  async obtenerDatosmesero(idCliente): Promise<DatosMesero[]> {
    let mesero: DatosMesero[] = [];
    //Opcion 1 es para obtener Datos Mesero
    this.servicioRestaurant.mostrarDetallesMesas({ 'idCliente': idCliente, 'Opcion': '1' }).subscribe(resp => {
      mesero.push(...Object.values(resp))
    })
    return mesero
  }
  async obtenerOrdenesCliente(idCliente):  Promise<DatosOrdenCliente[]> {
    let ordenesCliente: DatosOrdenCliente[] = [];
    //Opcion 2 es para obtener DetallesOrdenCliente
    this.servicioRestaurant.mostrarDetallesMesas({ 'idCliente': idCliente, 'Opcion': '2' }).subscribe(resp => {
      ordenesCliente.push(...Object.values(resp))
    })
    return ordenesCliente
  }


}
