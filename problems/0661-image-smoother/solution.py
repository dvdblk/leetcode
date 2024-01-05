class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """manual iteration over 3x3 neighborhood (fastest but bad)"""
        avg_img = []
        for i in range(len(img)):
            avg_row = []
            for j in range(len(img[i])):
                cur_sum = img[i][j]
                n_px = 1
                if i > 0:
                    if j > 0:
                        cur_sum += img[i-1][j-1]
                        n_px += 1
                    cur_sum += img[i-1][j]
                    n_px += 1
                    if j < len(img[i]) - 1:
                        cur_sum += img[i-1][j+1]
                        n_px += 1

                if j > 0:
                    cur_sum += img[i][j-1]
                    n_px += 1

                if j < len(img[i]) - 1:
                    cur_sum += img[i][j+1]
                    n_px += 1

                if i < len(img) - 1:
                    if j > 0:
                        cur_sum += img[i+1][j-1]
                        n_px += 1
                    cur_sum += img[i+1][j]
                    n_px += 1
                    if j < len(img[i]) - 1:
                        cur_sum += img[i+1][j+1]
                        n_px += 1

                avg_row.append(cur_sum//n_px)
            avg_img.append(avg_row)

        return avg_img

    def imageSmoother2(self, img: List[List[int]]) -> List[List[int]]:
        """iterate over the image and neighborhood for each px"""
        k = 3
        # result
        avg_img = []
        for i in range(len(img)):
            avg_row = []
            for j in range(len(img[i])):
                cur_sum = n_cells = 0

                # k x k neighborhood
                for i_k in range(-(k//2), 1+(k//2)):
                    for j_k in range(-(k//2), 1+(k//2)):
                        if i+i_k >= 0 and i+i_k < len(img) and j+j_k >= 0 and j+j_k < len(img[i]):
                            cur_sum += img[i+i_k][j+j_k]
                            n_cells += 1

                avg_row.append(cur_sum//n_cells)
            avg_img.append(avg_row)

        return avg_img