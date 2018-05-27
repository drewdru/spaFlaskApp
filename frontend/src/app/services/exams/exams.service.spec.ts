import { TestBed, inject } from '@angular/core/testing';

import { ExamsService } from './exams.service';

describe('ExamsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ExamsService]
    });
  });

  it('should be created', inject([ExamsService], (service: ExamsService) => {
    expect(service).toBeTruthy();
  }));
});
