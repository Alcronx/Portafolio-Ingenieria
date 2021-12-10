import { Component, OnInit } from '@angular/core';
import { MenuRestaurant } from 'src/app/interfaces/interfaces';
import { RestaurantAppService } from 'src/app/services/restaurant-app.service';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.page.html',
  styleUrls: ['./clientes.page.scss'],
})
export class ClientesPage implements OnInit {

  constructor(private servicioRestaurant: RestaurantAppService) { }
  menus: MenuRestaurant[] = []
  ngOnInit() {
    this.servicioRestaurant.obtenerMenuProducto().subscribe(resp => {
        this.menus.push(...Object.values(resp))
    })
  }

}
