import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MeseroPage } from './mesero.page';

const routes: Routes = [
  {
    path: '',
    component: MeseroPage
  },
  {
    path: 'mesas',
    loadChildren: () => import('../../Paginas/mesero/mesas/mesas.module').then( m => m.MesasPageModule)
  },
  {
    path: 'orden',
    loadChildren: () => import('../../Paginas/mesero/orden/orden.module').then( m => m.OrdenPageModule)
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MeseroPageRoutingModule {}
