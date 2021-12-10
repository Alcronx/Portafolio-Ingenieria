import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MeseroPageRoutingModule } from './mesero-routing.module';

import { MeseroPage } from './mesero.page';
import { ComponentesModule } from '../../componentes/componentes.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MeseroPageRoutingModule,
    ComponentesModule
  ],
  declarations: [MeseroPage]
})
export class MeseroPageModule {}
