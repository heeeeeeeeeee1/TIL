import { useEffect } from "react";
import useGetTopRatedMovies from "../hooks/useGetTopRatedMovies";
import "./MovieList.css";
import { useInView } from "react-intersection-observer";
import { Movie } from "../types/movies";

const MovieList = () => {
  // ref : 요소를 선택할 수 있는 능력
  // inView : 요소가 화면에 보이면 true, 아니면 false
  const { ref, inView } = useInView();

  const {
    data,
    isLoading,
    error,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useGetTopRatedMovies();

  // '더보기'가 보이는 순간 다시 fetchNextPage 호출
  useEffect(() => {
    console.log("화면에 있음?", inView);
    if (inView && hasNextPage && !isFetchingNextPage) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, isFetchingNextPage, fetchNextPage]);

  if (isLoading) return <div>로딩 중...</div>;
  if (error) return <div>에러가 발생했습니다!</div>;

  const allMovies = (data?.pages.flatMap((page) => page?.results) || []).filter(
    Boolean
  );

  const movieRows = [];

  for (let i = 0; i < allMovies.length; i += 4) {
    movieRows.push(allMovies.slice(i, i + 4));
  }

  return (
    <div className="container">
      {movieRows.map((row, rowIndex) => (
        <div key={rowIndex} className="movie-row">
          {row.map((movie: Movie) => (
            <div key={movie.id} className="movie-card">
              <img
                src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
                alt={movie.title}
                className="movie-poster"
              />
              <h3 className="movie-title">{movie.title}</h3>
            </div>
          ))}
        </div>
      ))}
      {hasNextPage && (
        <div ref={ref} className="load-more-btn">
          {isFetchingNextPage ? "로딩 중..." : "더 보기"}
        </div>
      )}
    </div>
  );
};

export default MovieList;
