Sau khi tải/pull về chạy lệnh sau:
git lfs migrate export --include="**.txt,**.prep"

Trước khi push lên nhớ chạy lệnh sau:
git lfs migrate import --include="*.txt,*.prep"

Lý do: vì có một số file lớn hơn 100mb không thể up lên git một cách thông thường được nên phải trước khi push phải chuyển sang dạng lfs, sau khi tải hoặc pull về phải export các file lfs để web có thể chạy bình thường.

Vô link này để biết thêm chi tiết: https://git-lfs.github.com/
