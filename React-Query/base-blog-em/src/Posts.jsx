import { useState } from "react";
import { useQuery } from "@tanstack/react-query"

import { fetchPosts, deletePost, updatePost } from "./api";
import { PostDetail } from "./PostDetail";
const maxPostPage = 10;

export function Posts() {
  const [currentPage, setCurrentPage] = useState(0);
  const [selectedPost, setSelectedPost] = useState(null);

  // useQuery는 옵션 객체를 받는다.
  // 쿼리 키 : 쿼리 캐시 내의 데이터 정의. 항상 배열임(v4이상)
  const {data, isError, error, isLoading} = useQuery({
    queryKey: ["posts"],
    queryFn: fetchPosts,  // 비동기 함수여서 결과 반환에 시간 걸림. 그 전까지는 데이터가 정의 되지 않음.
  })
  if (isLoading) { return <h3>로딩 중...</h3>}
  if (isError) {return <>
  <h3>흠... 뭔가 잘못되었군요...</h3><p>{error.toString()}</p> 
  </>
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
        <button disabled onClick={() => {}}>
          Previous page
        </button>
        <span>Page {currentPage + 1}</span>
        <button disabled onClick={() => {}}>
          Next page
        </button>
      </div>
      <hr />
      {selectedPost && <PostDetail post={selectedPost} />}
    </>
  );
}
