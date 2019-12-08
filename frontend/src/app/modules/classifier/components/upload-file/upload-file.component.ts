import { Component, ViewChild, ElementRef } from '@angular/core';

import { isMobile, scrollTo } from './../../../../shared/utils/helpers';
import { ClassificationService } from '../../services/classification.service';

class ImageSnippet {
  status: string = 'init';
  constructor(public src: string = 'https://via.placeholder.com/150', public file: File = null) { }
}

@Component({
  selector: 'upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.scss']
})
export class UploadFileComponent {
  private turned: boolean = false;
  private classified: boolean = false;
  private selectedFile: ImageSnippet = new ImageSnippet();
  private hasError: boolean = false;

  @ViewChild('fileInput', { static: false }) fileInput: ElementRef;

  constructor(private classifierService: ClassificationService) { }

  onFileSelected(files: FileList): void {
    const file: File = files.item(0);
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {
      this.selectedFile = new ImageSnippet(event.target.result, file);
      this.selectedFile.status = 'ok';
      this.turned = true;
    });

    reader.readAsDataURL(file);
  }

  onUpload(): void {
    const fb = new FormData();
    fb.append('image', this.selectedFile.file, this.selectedFile.file.name);
    
    this.classified = true;
    this.hasError = false;
    this.classifierService.predict(fb)
                          .subscribe(() => {
                            this.turned = true;
                            
                            if (isMobile) {
                              scrollTo(2500);
                            }
                          },
                          () => {
                            this.turned = false;
                            this.hasError = true;
                          });
  }

  onReset(): void {
    this.turned = false;
    this.classified = false;
    this.selectedFile = new ImageSnippet();
    this.classifierService.reset();
    this.fileInput.nativeElement.value = '';
  }
}
