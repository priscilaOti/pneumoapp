import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, throwError } from 'rxjs';
import { map, tap, retry, catchError } from 'rxjs/operators';

import { Classification } from './../models/classification';


@Injectable({
  providedIn: 'root'
})
export class ClassificationService {
  private readonly API_URL: string = 'https://pneumo-api.herokuapp.com/api/classifiers';
  public isLoading: boolean = false;

  private dataSource = new BehaviorSubject<Classification>(new Classification());
  data = this.dataSource.asObservable();

  constructor(private http: HttpClient) { }

  predict(image: FormData): Observable<Classification> {
    const url: string = `${this.API_URL}/predict/`;

    this.isLoading = true;

    return this.http.post(url, image)
      .pipe(tap(result => {
        this.dataSource.next(result as Classification);
        this.isLoading = false;
      }),
        retry(3),
        catchError(err => throwError(err)),
        map(result => result as Classification)
      );
  }

  reset(): void {
    this.dataSource.next(null);
  }
}
