import { Component, OnInit } from '@angular/core';

import { isMobile } from './../../../../shared/utils/helpers';
import { Classification } from './../../models/classification';
import { ClassificationService } from '../../services';

@Component({
  selector: 'chart-gauge',
  templateUrl: './chart-gauge.component.html',
  styleUrls: ['./chart-gauge.component.scss']
})
export class ChartGaugeComponent implements OnInit {
  private gaugeType: string = "arch";
  private gaugeValue: number = 0;
  private gaugeLabel: string = "";
  private gaugeAppendText: string = "%";
  private isMobile: boolean = isMobile;

  private thresholdConfig = {
    '0': { color: '#307fec' },
    '100': { color: '#307fec' }
  }

  constructor(private classifierService: ClassificationService) { }

  ngOnInit() {
    this.classifierService.data.subscribe((data: Classification) => {
      if (data) {
        this.gaugeLabel = data.prediction || "";
        this.gaugeValue = Number(((data.probabilities || {})[data.prediction] * 100).toFixed(2)) || 0;
      } else {
        this.gaugeLabel = "";
        this.gaugeValue = 0;
      }
    });
  }

}
