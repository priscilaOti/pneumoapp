import { NgModule, Directive } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgxGaugeModule } from 'ngx-gauge';

import { DirectivesModule } from '../../shared/directives';

import { ClassificationService } from './services';
import { UploadFileComponent, ChartGaugeComponent } from './components';

@NgModule({
  declarations: [
    UploadFileComponent,
    ChartGaugeComponent
  ],
  exports: [
    UploadFileComponent,
    ChartGaugeComponent
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    NgxGaugeModule,
    DirectivesModule
  ],
  providers: [
    ClassificationService
  ],
})
export class ClassifierModule { }
