import { useState, useEffect } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";

import { fetchPosts, deletePost, updatePost } from "./api";
import { PostDetail } from "./PostDetail";
const maxPostPage = 10;

export function Posts() {
  const [currentPage, setCurrentPage] = useState(1); // api 페이지 번호가 1부터니까
  const [selectedPost, setSelectedPost] = useState(null);

  const queryClient = useQueryClient();

  useEffect(() => {
    if (currentPage < maxPostPage) {
      const nextPage = currentPage + 1;
      queryClient.prefetchQuery({
        queryKey: ["posts", nextPage],
        queryFn: () => fetchPosts(nextPage),
      }); //useQuery에 사용된 것과 같은 형태의 쿼리키
    }
  }, [currentPage, queryClient]);

  // useQuery는 옵션 객체를 받는다.
  const { data, isError, error, isLoading } = useQuery({
    queryKey: ["posts", currentPage], // 쿼리 키 : 쿼리 캐시 내의 데이터 정의. 항상 배열임(v4이상)
    queryFn: () => fetchPosts(currentPage), // 익명함수를 사용해서 현재 페이지를 인자로 넘기기
    staleTime: 2000, // 2초
  });
  if (isLoading) {
    return <h3>로딩 중...</h3>;
  }
  if (isError) {
    return (
      <>
        <h3>흠... 뭔가 잘못되었군요...</h3>
        <p>{error.toString()}</p>
      </>
    );
  }

  return (
    <>
      <ul>
        {data.map((post) => (
          <li
            key={post.id}
            className="post-title"
            onClick={() => setSelectedPost(post)}
          >
            {post.title}
          </li>
        ))}
      </ul>
      <div className="pages">
        <button
          disabled={currentPage <= 1}
          onClick={() => {
            setCurrentPage((previousValue) => previousValue - 1);
          }}
        >
          Previous page
        </button>
        <span>Page {currentPage + 1}</span>
        <button
          disabled={currentPage >= maxPostPage}
          onClick={() => {
            setCurrentPage((previousValue) => previousValue + 1);
          }}
        >
          Next page
        </button>
      </div>
      <hr />
      {selectedPost && <PostDetail post={selectedPost} />}
    </>
  );
}
