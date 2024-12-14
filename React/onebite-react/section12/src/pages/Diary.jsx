import { useParams } from "react-router-dom" // 현재 브라우저에 명시한 URL Parameter의 값을 가져오는 커스텀 훅
const Diary = () => {
  const params = useParams()

  return <div>{params.id}번 일기</div>
}

export default Diary