import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {map, catchError} from 'rxjs/operators';
import {API_URL} from '../../env';
import {Exam} from '../../models/exam.model';

@Injectable({
  providedIn: 'root'
})
export class ExamsService {

  constructor(private http: HttpClient) { 

  }
  
  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http.get(`${API_URL}/exams`)
    .pipe(
        map((res:Exam[]) => res), // or any other operator
        catchError(error => {
            console.log(`Bad Promise: ${error}`);
            return [];
        })
    );
  }
}
