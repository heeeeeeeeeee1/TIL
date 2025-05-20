export interface MovieResponse {
  page: number;
  total_pages: number;
  results: Movie[];
}

export interface Movie {
  id: number;
  title: string;
  poster_path: string;
}
