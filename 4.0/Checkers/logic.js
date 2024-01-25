class UpdateBoard {
    constructor(board) {
      this.board = [...board];
    }
  
    validMoves(arr) {
      if (Array.isArray(arr)) {
        for (let m of arr) {
          const { to } = m;
          this.board[to.y][to.x] = "X";
        }
        console.log(this.board);
        return this.board;
      }
    }
    moveCapture({ from, to, capture }) {
      let piece = this.board[from.y][from.x];
      this.board[to.y][to.x] = piece;
      this.board[from.y][from.x] = "";
      this.board[capture.y][capture.x] = "";
      return this.board;
    }
  
    moveOnly({ from, to }) {
      let piece = this.board[from.y][from.x];
      this.board[to.y][to.x] = piece;
      this.board[from.y][from.x] = "";
      return this.board;
    }
  
    anlizeBoard() {
      let B = 0;
      let W = 7;
  
      let blackArr = this.board[B];
      let whiteArr = this.board[W];
  
      // Black Piece
      for (let i = 0; i < blackArr.length; i++) {
        let piece = blackArr[i];
        if (piece === "B") {
          this.board[B][i] = "KB";
        }
      }
    }
  }
  
  module.exports = UpdateBoard;