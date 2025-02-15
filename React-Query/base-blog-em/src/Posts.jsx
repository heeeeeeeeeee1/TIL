import { useState } from "react";
import { useQuery } from "@tanstack/react-query"

import { fetchPosts, deletePost, updatePost } from "./api";
import { PostDetail } from "./PostDetail";
const maxPostPage = 10;

export function Posts() {
  const [currentPage, setCurrentPage] = useState(0);
  const [selectedPost, setSelectedPost] = useState(null);

  // replace with useQuery.
  // const data = [];
  // useQuery는 옵션 객체를 받는다.
  // 쿼리 키 : 쿼리 캐시 내의 데이터 정의. 항상 배열임(v4이상)
  const {data} = useQuery({
    queryKey: ["posts"],
    queryFn: fetchPosts,  // 비동기 함수여서 결과 반환에 시간 걸림. 그 전까지는 데이터가 정의 되지 않음.
  })
  // 해결 할 수 있는 리액트 쿼리 도구가 많지만 일단은 사용 안함
  if (!data) { return <div />}

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
