import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MenuRestaurant, Mesa, Mesero, MenuRestaurantCarrito } from '../interfaces/interfaces';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestaurantAppService {

  private carrito = [];
  private carritoNumeroItems = new BehaviorSubject(0);
  public ipGlobal = "";
  constructor(private http: HttpClient) { }

  obtenerMenuProducto() {
    console.log('http://'+this.ipGlobal+':8000/RestaurantApi/Menu?format=json')
    return this.http.get<MenuRestaurant>('http://'+this.ipGlobal+':8000/RestaurantApi/Menu?format=json');
  }

  obtenerMesa() {
    console.log('http://'+this.ipGlobal+':8000/RestaurantApi/Menu?format=json')
    return this.http.get<Mesa>('http://'+this.ipGlobal+':8000/RestaurantApi/Cliente?format=json');
  }

  obtenerMeseros() {
    console.log('http://'+this.ipGlobal+':8000/RestaurantApi/Menu?format=json')
    return this.http.get<Mesero>('http://'+this.ipGlobal+':8000/RestaurantApi/Mesero?format=json');
  }

  agregarOrdenCliente(data) {
    console.log('http://'+this.ipGlobal+':8000/RestaurantApi/Menu?format=json')
    return this.http.post('http://'+this.ipGlobal+':8000/RestaurantApi/Orden',data);
  }

  mostrarDetallesMesas(data) {
    return this.http.post('http://'+this.ipGlobal+':8000/RestaurantApi/DetallesMesa',data); 
  }

  pagarOrdenCliente(data) {
    return this.http.post('http://'+this.ipGlobal+':8000/RestaurantApi/PagarOrdenApi',data); 
  }

  //Carrito de compras

  obtenerCarrito() {
    return this.carrito;
  }

  PonerIPServicio(ip) {
    this.ipGlobal = ip;
  }

  obtenerCarritoNumeroItems() {
    return this.carritoNumeroItems;
  }

  bajarCantidadProducto(producto) {
    for (let [index, p] of this.carrito.entries()) {
      if (p.menuid === producto.menuid) {
        p.quantity -= 1;
        p.total = p.menuPrice * p.quantity; 
        if (p.quantity == 0) {
          this.carrito.splice(index, 1)
        }
      }

    }

    this.carritoNumeroItems.next(this.carritoNumeroItems.value - 1);
  }

  eliminarProducto(producto) {
    for (let [index, p] of this.carrito.entries()) {
      if (p.id === producto.id) {
        this.carritoNumeroItems.next(this.carritoNumeroItems.value - p.cantidad);
        this.carrito.splice(index, 1);
      }
    }
  }

  eliminarCarrito(){
    this.carrito = [];
  }

  agregarProducto(producto) {
    let agregado = false;
    for (let p of this.carrito) {
      if (p.menuid === producto.menuid) {
        p.quantity += 1;
        p.total = p.menuPrice * p.quantity;
        agregado = true;
      }
    }
    if (!agregado) {
      this.carrito.push(producto);
    }
    this.carritoNumeroItems.next(this.carritoNumeroItems.value + 1);
  }

}
