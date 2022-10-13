from pdiff import diff_pdf


if __name__ == '__main__':
    dt = diff_pdf(f1='/diff-pdf/_tests/test_2/in_file_2.pdf',
                f2='/diff-pdf/_tests/test_2/in_file_1.pdf',
                do_cache=True)
    print(dt)