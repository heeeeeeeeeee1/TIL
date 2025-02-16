import { fetchComments } from "./api";
import "./PostDetail.css";
import { useQuery } from "@tanstack/react-query";

export function PostDetail({ post }) {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["comments", post.id], // ["coments"] 로 하면 post가 달라져도 같은 comments만 뜸
    queryFn: () => fetchComments(post.id),
  });

  if (isLoading) {
    return <h3>로딩중</h3>;
  }

  if (isError) {
    return (
      <>
        <h3>에러</h3>
        <p>{error.toString()}</p>
      </>
    );
  }

  return (
    <>
      <h3 style={{ color: "blue" }}>{post.title}</h3>
      <button>Delete</button> <button>Update title</button>
      <p>{post.body}</p>
      <h4>Comments</h4>
      {data.map((comment) => (
        <li key={comment.id}>
          {comment.email}: {comment.body}
        </li>
      ))}
    </>
  );
}
