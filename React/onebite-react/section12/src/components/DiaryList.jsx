import "./DiaryList.css"
import Button from "./Button"
import DiaryItem from "./DiaryItem"

const DiaryList = () => {
  return (
    <div className="DiaryList">
      {/* 메뉴바 */}
      <div className="menu_bar">
        <select>
          {/* option 설정에 value 별도로 설정해주는 이유 : 어떤 옵션이 선택되어 있는지 state이용해서 저장해야함*/}
          {/* state값에 한국어나 공백 입력하는 것 보다는 영어로 작업하는 것이 나아서 */}
          <option value={"latest"}>최신순</option>
          <option value={"oldest"}>오래된순</option>          
        </select>
        <Button text={"새 일기 쓰기"} type={"POSITIVE"} />
      </div>
      {/* 다이어리 리스트 */}
      <div className="list_wrapper"></div>
      <DiaryItem />
    </div>
  )
}

export default DiaryList