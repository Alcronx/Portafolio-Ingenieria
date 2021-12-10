import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { HeaderComponent } from './header/header.component';
import { ModalMesasComponent } from './modal-mesas/modal-mesas.component';
import { IpGlobalComponent } from './ip-global/ip-global.component';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    HeaderComponent,
    ModalMesasComponent,
    IpGlobalComponent
  ],
  exports:[
    HeaderComponent,
    ModalMesasComponent,
    IpGlobalComponent
  ],
  imports: [
    CommonModule,
    IonicModule,
    FormsModule
  ]
})
export class ComponentesModule { }
