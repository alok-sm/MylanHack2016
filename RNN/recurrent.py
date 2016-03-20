import numpy as np

def load(file_name):
    import pickle
    with open(file_name) as f:
     return pickle.load(f)

class RNN:
    def __init__(self, stages, hidden, input_size, output_size, learning_rate = 1e-1):
        self.hidden_size = hidden 
        self.seq_length = stages 
        self.learning_rate = learning_rate
        self.input_size = input_size
        self.output_size = output_size

        # model parameters
        self.Wxh = np.random.randn(self.hidden_size, self.input_size)*0.01 
        self.Whh = np.random.randn(self.hidden_size, self.hidden_size)*0.01 
        self.Why = np.random.randn(self.output_size, self.hidden_size)*0.01 
        self.bh = np.zeros((self.hidden_size, 1))
        self.by = np.zeros((self.output_size, 1))
        
    def feedForward(self, inputs, hprev = None):
        '''
            Returns the softmax probability for the given classes
        '''
        if hprev is None:
            hprev = np.zeros((self.hidden_size,1))
        self.xs, self.hs, self.ys, self.ps = {}, {}, {}, {}
        self.hs[-1] = np.copy(hprev)
        for t in xrange(len(inputs)):
            self.xs[t] = np.reshape(inputs[t], (self.input_size,1))
            self.hs[t] = np.tanh(np.dot(self.Wxh, self.xs[t]) + np.dot(self.Whh, self.hs[t-1]) + self.bh) 
            self.ys[t] = np.dot(self.Why, self.hs[t]) + self.by 
            self.ps[t] = np.exp(self.ys[t]) / np.sum(np.exp(self.ys[t]))
        return self.ps[len(inputs)-1], self.hs[len(inputs)-1]
    
    def backProp(self, targets = None, dhnext = None):
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        if dhnext is None: dhnext = np.zeros_like(self.hs[0])
        
        for t in reversed(xrange(len(self.xs))):
            dy = np.copy(self.ps[t])
            dy = np.copy(self.ps[t])
            dy[targets[t]] -= 1
            dWhy += np.dot(dy, self.hs[t].T)
            dby += dy
            dh = np.dot(self.Why.T, dy) + dhnext
            dhraw = (1 - self.hs[t] * self.hs[t]) * dh
            dbh += dhraw
            dWxh += np.dot(dhraw, self.xs[t].T)
            dWhh += np.dot(dhraw, self.hs[t-1].T)
            dhnext = np.dot(self.Whh.T, dhraw)
        for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
            np.clip(dparam, -5, 5, out=dparam)
        return dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]

    def lossFun(self, inputs, hprev=None, targets = None, dhnext = None):
        if hprev is None: hprev = np.zeros((self.hidden_size,1))
        xs, hs, ys, ps = {}, {}, {}, {}
        hs[-1] = np.copy(hprev)
        # print hs[-1].shape, hprev.size
        loss = 0

        for t in xrange(len(inputs)):
            xs[t] = np.reshape(inputs[t], (self.input_size,1))
            hs[t] = np.tanh(np.dot(self.Wxh, xs[t]) \
            + np.dot(self.Whh, hs[t-1]) +\
            self.bh)
            ys[t] = np.dot(self.Why, hs[t]) + self.by 
            ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) 
            # loss += -np.log(ps[t][targets[t],0])

        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        if dhnext is None: dhnext = np.zeros_like(hs[0])
        
        for t in reversed(xrange(len(inputs))):
            dy = np.copy(ps[t])
            dy[targets[t]] -= 1
            dWhy += np.dot(dy, hs[t].T)
            dby += dy

            dh = np.dot(self.Why.T, dy) + dhnext
            dhraw = (1 - hs[t] * hs[t]) * dh
            dbh += dhraw
            dWxh += np.dot(dhraw, xs[t].T)
            dWhh += np.dot(dhraw, hs[t-1].T)
            dhnext = np.dot(self.Whh.T, dhraw)
        for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
            np.clip(dparam, -5, 5, out=dparam)
        return loss, dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]


    def train(self, input_i, target, epochs = 10):
        n, p, counter = 0, 0, 0
        mWxh, mWhh, mWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        mbh, mby = np.zeros_like(self.bh), np.zeros_like(self.by)
        smooth_loss = -np.log(1.0/self.output_size)*self.seq_length
        
        while n<epochs:
            for input in input_i:
                if p >= len(input) - (len(input)%self.seq_length) or n == 0: 
                    hprev = np.zeros((self.hidden_size,1))
                    # print hprev
                    p = 0
                    n += 1
                inputs = input[p:p+self.seq_length]
                targets = target[p:p+self.seq_length]

                loss, dWxh, dWhh, dWhy, dbh, dby, hprev = self.lossFun(inputs, targets = targets, hprev = hprev)
                smooth_loss = smooth_loss * 0.999 + loss * 0.001
                
                if p == 0: print 'epoch %d, loss: %f' % (n, smooth_loss)
                
                for param, dparam, mem in zip([self.Wxh, self.Whh, self.Why, self.bh, self.by], 
                                            [dWxh, dWhh, dWhy, dbh, dby], 
                                            [mWxh, mWhh, mWhy, mbh, mby]):
                    mem += dparam * dparam
                    param += -self.learning_rate * dparam / np.sqrt(mem + 1e-8)

                p += self.seq_length
                print "Epoch = %d, Iteration = %d"%(n,counter)
                counter += 1
        return
    
    def updateParams(self, gradients):
        mWxh, mWhh, mWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        mbh, mby = np.zeros_like(self.bh), np.zeros_like(self.by)
        for param, dparam, mem in zip([self.Wxh, self.Whh, self.Why, self.bh, self.by], 
                                    gradients, 
                                    [mWxh, mWhh, mWhy, mbh, mby]):
            mem += dparam * dparam
            param += -self.learning_rate * dparam / np.sqrt(mem + 1e-8)
    
    def save(self, file_name):
        import pickle
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        return    
    
if __name__ == "__main__":
    '''
        Random code
    '''
    import random
    temp = [[(random.randint(2,20)+(n-1)*2) for n in range(1,100)] for i in range(1000)] # [a+(n-1)*d]
    outputs = []
    vocab = []
    for i in temp:
        t = [j for j in i if j<128]
        outputs.append(t)
        vocab.extend(t)
    vocab = [i for i in range(128)]
    rnn = RNN(100,30,7,len(vocab))
    
    def fun(x):
        l = [0]*7
        t = list(map(int,[c for c in bin(x)[2:]]))
        l[len(l)-len(t):] = t
        return l
    
    inputs = [list(map(fun,outputs[i])) for i in range(len(outputs))]
    # print inputs[0]
    for i in range(3):
        for j in range(len(inputs)):
            p = rnn.lossFun(inputs[j][:-1],targets=outputs[j][1:])
            rnn.updateParams(p[1:-1])
    print "done"
    rnn.save("test_rnn.pickle")
    rnn = load("test_rnn.pickle")
    while True:
        test = list(map(fun,eval(raw_input("Enter sequence as list:"))))
        res = rnn.feedForward(test)
        print res[0].tolist().index(max(res[0])),max(res[0]), min(res[0])