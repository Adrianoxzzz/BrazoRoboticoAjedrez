import chess
import chess.engine
import serial

ser = serial.Serial('COM4',115200)
board = chess.Board();
print(board);
print("\n")
while not board.is_game_over():
    jugada = input()
    board.push_san(jugada)
    actualboard = board
    engine= chess.engine.SimpleEngine.popen_uci(r"C:\stockfish-windows-x86-64-sse41-popcnt\stockfish\stockfish-windows-x86-64-sse41-popcnt");
    limit = chess.engine.Limit(time = 2.0)
    result = engine.play(board,limit)
    board.push(result.move);
    fen = board.fen()
    ser.write(fen.encode('utf8'))
    ser.write(b'l')
    test = ser.read_until('l')
    print(test)
    print("\n")
    print(fen)
    print("\n")
    print(board);
    print("\n")
    engine.quit();
