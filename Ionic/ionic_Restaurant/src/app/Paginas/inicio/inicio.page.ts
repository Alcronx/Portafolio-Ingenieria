import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { IpGlobalComponent } from 'src/app/componentes/ip-global/ip-global.component';

interface Componete {
  icon: string;
  name: string;
  redirectTo: string;
}

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.page.html',
  styleUrls: ['./inicio.page.scss'],
})
export class InicioPage implements OnInit {

  compontes: Componete[] = [
    {
      icon: "body-outline",
      name: "Cliente",
      redirectTo: "/clientes",
    },
    {
      icon: "beer-outline",
      name: "Mesero",
      redirectTo: "/mesero",
    },
  ]

  

  constructor(public modalController: ModalController,) { }

  ngOnInit() {
  }

  async AbrirmodalOpciones() {
    const modal = await this.modalController.create({
      component: IpGlobalComponent,
      cssClass: 'my-custom-class'
    });
    return await modal.present();
  }
}


