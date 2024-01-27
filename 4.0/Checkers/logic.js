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
  
  
  //module.exports = UpdateBoard;