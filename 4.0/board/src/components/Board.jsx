// Board.js
import React from 'react';
import Cell from './Cell';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import Piece from './Piece';

function Board() {
  const handlePieceDrop = (color, rowIndex, colIndex) => {
    // Handle the drop event logic here, e.g., updating the position of the piece.
    console.log(`Piece dropped at row ${rowIndex}, column ${colIndex} with color ${color}`);
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="board">
        {Array(8).fill(null).map((row, rowIndex) => (
          <div key={rowIndex} className="board-row">
            {Array(8).fill(null).map((col, colIndex) => {
              const isDarkSquare = (rowIndex + colIndex) % 2 === 1;
              const cellValue = `${rowIndex}${colIndex}`;

              // Place black pieces at the top
              if (rowIndex < 2 && colIndex % 3 === 0) {
                return (
                  <Cell key={`${rowIndex}-${colIndex}`} value={cellValue} isDark={isDarkSquare} rowIndex={rowIndex} colIndex={colIndex} onPieceDrop={handlePieceDrop}>
                    <Piece color="black" />
                  </Cell>
                );
              }

              // Place white pieces at the bottom
              if (rowIndex > 5 && colIndex % 3 === 0) {
                return (
                  <Cell key={`${rowIndex}-${colIndex}`} value={cellValue} isDark={isDarkSquare} rowIndex={rowIndex} colIndex={colIndex} onPieceDrop={handlePieceDrop}>
                    <Piece color="white" />
                  </Cell>
                );
              }

              return <Cell key={`${rowIndex}-${colIndex}`} value={cellValue} isDark={isDarkSquare} rowIndex={rowIndex} colIndex={colIndex} onPieceDrop={handlePieceDrop} />;
            })}
          </div>
        ))}
      </div>
    </DndProvider>
  );
}

export default Board;




