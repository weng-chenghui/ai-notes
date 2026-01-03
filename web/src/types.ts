export interface DocumentFile {
  name: string;
  type: 'pdf' | 'html';
}

export interface Document {
  dir: string;
  title: string;
  files: DocumentFile[];
}

export interface Manifest {
  generated: string;
  commit: string;
  documents: Document[];
}
