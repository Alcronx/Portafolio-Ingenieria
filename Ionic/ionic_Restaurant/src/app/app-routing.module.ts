import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'inicio',
    loadChildren: () => import('./Paginas/inicio/inicio.module').then( m => m.InicioPageModule)
  },
  {
    path: 'clientes',
    loadChildren: () => import('./Paginas/clientes/clientes.module').then( m => m.ClientesPageModule)
  },
  {
    path: 'mesero',
    loadChildren: () => import('./Paginas/mesero/mesero.module').then( m => m.MeseroPageModule)
  },
  {
    path: '',
    redirectTo: 'inicio',
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
