class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prev_row_devices = 0
        laser_beams = 0
        ROWS, COLS = len(bank), len(bank[0])
        
        for r in range(ROWS):
            cur_row_devices = 0
            for c in range(COLS):
                if bank[r][c] == '1':
                    cur_row_devices += 1
            if cur_row_devices:
                laser_beams += (cur_row_devices * prev_row_devices)
                prev_row_devices = cur_row_devices
        
        return laser_beams
        