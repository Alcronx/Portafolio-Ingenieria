import { Component, OnInit } from '@angular/core';


interface ComponeteMesero {
  icon: string;
  name: string;
  redirectTo: string;
}

@Component({
  selector: 'app-mesero',
  templateUrl: './mesero.page.html',
  styleUrls: ['./mesero.page.scss'],
})
export class MeseroPage implements OnInit {
  
  compontes: ComponeteMesero[] = [
    {
      icon: "layers-outline",
      name: "Mesas",
      redirectTo: "/mesero/mesas",
    },
    {
      icon: "clipboard-outline",
      name: "Orden",
      redirectTo: "/mesero/orden",
    },
  ]
  constructor() { }

  ngOnInit() {
  }

}
