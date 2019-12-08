import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HomeComponent } from './home.component';

import { ComponentsModule } from '../../shared/components';
import { ClassifierModule } from './../../modules/classifier';

@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    ClassifierModule
  ]
})
export class HomeModule { }
