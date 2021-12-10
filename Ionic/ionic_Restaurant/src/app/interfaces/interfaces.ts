export interface MenuRestaurant {
  menuid: number;
  name: string;
  recipe: string;
  cookingtime: string;
  menucost: number;
  menuprice: number;
  state: string;
}

export interface Mesero {
  waiterid: number;
  rut: string;
  name1: string;
  name2: string;
  lastname1: string;
  lastname2: string;
  state: string;
}

export interface Mesa {
  tableid: number;
  tableNumber: number;
  tableMembers: number;
  aviable: string;
  state: string;
  rt_tableid_related: Cliente[];
}

export interface Cliente {
  clientid: number;
  name: string;
  members: number;
  state: string;
  rt_tableid: number;
}

export class MenuRestaurantCarrito {
  menuid: number;
  name: string;
  menuPrice: number;
  quantity: number;
  total: number;
}


export class OrderClient {
  idMesero: number;
  idCliente: number;
  totalCarrito: number;
  OrderClientDetails: MenuRestaurantCarrito[];
}


export interface DatosMesero {
  WAITERID: number;
  CLIENTID: number;
  NAMECLIENT: string;
  NAMEWAITER: string;
  LASTNAMEWAITER: string;
  ESTADO_CLIENTE: string;
  ESTADO_ORDENCLIENTE: string;
  ESTADO_MESERO: string;
}

export interface DatosOrdenCliente {
  ORDECLIENTID: number;
  CLIENT_CLIENTID: number;
  WAITER_WAITERID: number;
  MENUID: number;
  QUIANTITY: number;
  TOTAL: number;
  ORDERCLIENTTOTAL: number;
  NAME: string;
  STATEORDERSTATE: string;
  STATEORDERCLIENT: string;
}






