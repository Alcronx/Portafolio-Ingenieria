import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MesasPageRoutingModule } from './mesas-routing.module';

import { MesasPage } from './mesas.page';
import { ComponentesModule } from 'src/app/componentes/componentes.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MesasPageRoutingModule,
    ComponentesModule,
  ],
  declarations: [MesasPage]
})
export class MesasPageModule {}
