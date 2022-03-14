#
# Write a rectilinear grid to ASCII Tecplot format.
#
def tecplot_WriteRectilinearMesh(filename, X, Y, Z, vars):
    def pad(s, width):
        s2 = s
        while len(s2) < width:
            s2 = ' ' + s2
        if s2[0] != ' ':
            s2 = ' ' + s2
        if len(s2) > width:
            s2 = s2[:width]
        return s2

    def varline(vars, id, fw):
        s = ""
        for v in vars:
            s = s + pad(estr(v[1][id]), fw)
        s = s + '\n'
        return s

    def estr(v):
        return "%.6E" % v

    fw = 15  # field width

    f = open(filename, "wt")

    f.write('Variables="X","Y"')
    if len(Z) > 0:
        f.write(',"Z"')
    for v in vars:
        f.write(',"%s"' % v[0])
    f.write('\n\n')

    f.write('Zone I=' + pad(str(len(X)), 6) + ',J=' + pad(str(len(Y)), 6))
    if len(Z) > 0:
        f.write(',K=' + pad(str(len(Z)), 6))
    f.write(', F=POINT\n')

    if len(Z) > 0:
        id = 0
        for k in range(len(Z)):
            for j in range(len(Y)):
                for i in range(len(X)):
                    f.write(pad(estr(X[i]), fw) + pad(estr(Y[j]), fw) + pad(estr(Z[k]), fw))
                    f.write(varline(vars, id, fw))
                    id = id + 1
    else:
        id = 0
        for j in range(len(Y)):
            for i in range(len(X)):
                f.write(pad(estr(X[i]), fw) + pad(estr(Y[j]), fw))
                f.write(varline(vars, id, fw))
                id = id + 1

    f.close()
