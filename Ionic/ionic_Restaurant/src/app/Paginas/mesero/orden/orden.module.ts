import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { OrdenPageRoutingModule } from './orden-routing.module';

import { OrdenPage } from './orden.page';
import { ComponentesModule } from 'src/app/componentes/componentes.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    OrdenPageRoutingModule,
    ComponentesModule,
  ],
  declarations: [OrdenPage]
})
export class OrdenPageModule {}
