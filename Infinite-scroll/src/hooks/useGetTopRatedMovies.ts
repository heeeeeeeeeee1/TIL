import { useInfiniteQuery } from "@tanstack/react-query";

const fetchTopRatedMovies = async (page: number) => {
  const response = await fetch(
    `https://api.themoviedb.org/3/movie/top_rated?api_key=${
      import.meta.env.VITE_API_KEY
    }&page=${page}`
  );
  return response.json();
};

const useGetTopRatedMovies = () => {
  return useInfiniteQuery({
    queryKey: ["top-rated-movies"], // 쿼리 이름
    queryFn: ({ pageParam }) => {
      return fetchTopRatedMovies(pageParam);
    },
    // last : 지난 번에 받아온 데이터 값을 읽어올 수 있음
    // 페이지 1번을 호출한 경우, 1번 호출한 결괏값을 last에 넘겨줌
    getNextPageParam: (last) => {
      // 지난번에 받았던 페이지 정보가 총 페이지 수보다 작으면 다음 페이지 호출
      if (last.page < last.total_pages) {
        return last.page + 1; // 이 return한 값이 pageParam에 들어감
      }
      return undefined; // 더 이상 페이지가 없으면 undefined 반환
    },
    initialPageParam: 1, // 첫 번째 페이지 호출 -> pageParam에 1이 들어감 -> fetchTopRatedMovies(1) 호출
  });
};

export default useGetTopRatedMovies;
