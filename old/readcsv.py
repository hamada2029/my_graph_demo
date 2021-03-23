"""Csv class."""
import os
import io
import csv


def replace_newline(txt):
    if '\r' in txt and '\n' in txt:  # CRLF2LF
        print('CRLF')
        txt = txt.replace('\r\n', '\n')
        txt = txt.replace('\r', '\n')
    elif '\r' in txt:  # CR2LF
        print('CR')
        txt = txt.replace('\r', '\n')
    return txt


class CsvObj:
    """Csv class."""

    def __init__(self, fpath):
        """__Init__."""
        self.fpath = fpath
        self.dics = None
        self.headers = None

    def read(self):
        """Read csv file."""
        if not os.path.exists(self.fpath):
            return

        with open(self.fpath, 'rb') as fob:
            bin_s = fob.read()

        for enc in ['utf-8-sig', 'cp932', 'utf-16-le']:
            try:
                txt = bin_s.decode(enc)
                print(enc)
                break
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError('decode')

        txt = replace_newline(txt)

        with io.StringIO(txt) as fob:
            reader = csv.reader(fob)
            lines = [line for line in reader]

        if not lines:
            return  # 空

        self.headers = lines[0]
        self.dics = []

        for line in lines[1:]:
            zipped = zip(self.headers, line)
            dic = dict(zipped)
            self.dics.append(dic)

    def write(self):
        """Write csv file."""
        lines = [self.headers]

        for dic in self.dics:
            line = [dic[h] for h in self.headers]  # headers順
            lines.append(line)

        # with open(self.fpath, 'wb') as fob:
        #     fob.write(b'\xff\xfe')  # BOM
        # with open(self.fpath, 'a', encoding='utf-16-le') as fob:

        with open(self.fpath, 'w', encoding='cp932') as fob:
            writer = csv.writer(
                fob,
                lineterminator='\n',
                quoting=csv.QUOTE_ALL
            )
            writer.writerows(lines)

    def update(self, ukey, newdic):
        """一意なキーでアップデート."""
        for dic in self.dics:
            if dic[ukey] == newdic[ukey]:
                dic = newdic
                return


def main():
    """Main function."""


if __name__ == "__main__":
    main()
