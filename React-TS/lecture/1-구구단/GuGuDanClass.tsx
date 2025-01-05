import * as React from 'react';
import { Component } from 'react';
// react에서 hook 사용을 권장하긴 함

interface State {
  first: number;
  second: number;
  value: string;
  result: string;
}

class GuGuDan extends Component<{}, State> {
  input: HTMLInputElement | null = null;

  state = {
    first: Math.ceil(Math.random() * 9),
    second: Math.ceil(Math.random() * 9),
    value: '',
    result: '',
  };

  // onRefInput 함수
  onRefInput = (c: HTMLInputElement) => {
    this.input = c;
  };

  // onChange 이벤트 핸들러
  onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ value: e.target.value });
  };

  // onSubmit 이벤트 핸들러
  onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const { first, second, value } = this.state;

    if (parseInt(value) === first * second) {
      this.setState({
        result: `정답: ${value}`,
        first: Math.ceil(Math.random() * 9),
        second: Math.ceil(Math.random() * 9),
        value: '',
      });
      if (this.input) this.input.focus();
    } else {
      this.setState({
        result: '땡',
        value: '',
      });
      if (this.input) this.input.focus();
    }
  };

  // render 메서드
  render() {
    const { first, second, value, result } = this.state;

    return (
      <>
        <div>
          {first} 곱하기 {second}는?
        </div>
        <form onSubmit={this.onSubmit}>
          <input
            ref={this.onRefInput}
            type="number"
            value={value}
            onChange={this.onChange}
          />
          <button>입력!</button>
        </form>
        <div>{result}</div>
      </>
    );
  }
}

export default GuGuDan;
